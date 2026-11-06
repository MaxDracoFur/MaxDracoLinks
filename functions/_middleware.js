// One canonical host: www.maxdraco.com -> 301 https://maxdraco.com (same path + query).
// Card seo-titles-dupes-404. Static assets skip this (public/_routes.json excludes them),
// so it only runs for pages and /api/*.
export async function onRequest ({ request, next }) {
  const url = new URL(request.url)
  if (url.hostname === 'www.maxdraco.com') {
    url.hostname = 'maxdraco.com'
    url.protocol = 'https:'
    url.port = ''
    return Response.redirect(url.toString(), 301)
  }
  return next()
}
