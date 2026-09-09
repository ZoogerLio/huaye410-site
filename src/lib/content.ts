export function withBase(path: string) {
  if (/^(https?:|mailto:|tel:|#)/.test(path)) return path;
  const base = import.meta.env.BASE_URL;
  return `${base}${path.replace(/^\/+/, '')}`;
}

export function externalLinkProps(url: string) {
  return /^https?:/.test(url) ? { target: '_blank', rel: 'noreferrer' } : {};
}
