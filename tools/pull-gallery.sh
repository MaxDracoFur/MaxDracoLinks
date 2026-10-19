#!/bin/sh
# Mirror Stage's Gallery exports into assets/gallery/ (gitignored).
# Stage writes stripped copies to the NAS: general/stage/outbox/maxdraco-gallery/<album>/.
# Shows exactly what would change and asks before copying anything.
# Read-only on the NAS side; nothing is written to fat.
set -eu
cd "$(dirname "$0")/.."
SRC=fat:/mnt/migrate/k8s-dst/general/stage/outbox/maxdraco-gallery/
FILTER="--include=*/ --include=*.jpg --include=trip.json --exclude=*"
# The outbox belongs to Stage's uid (0750), so read it with sudo on fat. Read-only.
RS="--rsync-path=sudo -n rsync"
mkdir -p assets/gallery

if ! ssh fat 'sudo -n test -d /mnt/migrate/k8s-dst/general/stage/outbox/maxdraco-gallery'; then
  echo "No Gallery exports in Stage yet (or the NAS isn't reachable). Nothing copied."
  echo "In Stage: tag photos 'maxdraco.com / Gallery', then press Export on the trip."
  exit 1
fi

# Never report "up to date" unless the read actually succeeded.
if ! PLAN=$(rsync -a --delete --dry-run --itemize-changes "$RS" $FILTER "$SRC" assets/gallery/ 2>&1); then
  echo "Could not read Stage's Gallery exports. Nothing copied. rsync said:"
  echo "$PLAN"
  exit 1
fi
CHANGES=$(echo "$PLAN" | grep -E '^(>f|\*deleting)' || true)
if [ -z "$CHANGES" ]; then
  echo "Gallery is already up to date with Stage. Nothing to do."
  exit 0
fi

echo "These changes would be made to the gallery (album/file):"
echo "$CHANGES" | sed -E 's/^>f[^ ]* /  ADD     /; s/^\*deleting +/  REMOVE  /'
echo
printf "Copy these into the site? [y/N] "
read -r answer
case "$answer" in
  y|Y|yes) ;;
  *) echo "Nothing copied."; exit 1 ;;
esac

rsync -a --delete "$RS" $FILTER "$SRC" assets/gallery/
echo "Done. albums: $(find assets/gallery -name trip.json | wc -l | tr -d ' ')  photos: $(find assets/gallery -name '*.jpg' | wc -l | tr -d ' ')"
echo "Next: hugo --gc --cleanDestinationDir, check http://localhost:1313/gallery/ with 'hugo server', then ./deploy-cloudflare.sh"
