#!/bin/sh
# Mirror Stage's Gallery exports into assets/gallery/ (gitignored), then build.
# Stage writes stripped copies to the NAS: general/stage/outbox/maxdraco-gallery/<album>/.
# Read-only on the NAS side; nothing is written to fat.
set -eu
cd "$(dirname "$0")/.."
rsync -a --delete --include='*/' --include='*.jpg' --include='trip.json' --exclude='*' \
  fat:/mnt/migrate/k8s-dst/general/stage/outbox/maxdraco-gallery/ assets/gallery/
echo "albums: $(find assets/gallery -name trip.json | wc -l | tr -d ' ')  photos: $(find assets/gallery -name '*.jpg' | wc -l | tr -d ' ')"
