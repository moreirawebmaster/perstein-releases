# Changelog

Cada arquivo é `changelog/<produto>/<versão>.json`. A versão é semver sem `v`
e sem revisão de build. O arquivo entra no mesmo commit da tag
`<produto>-v<versão>`.

```json
{
  "product": "desktop",
  "version": "1.0.18",
  "publishedAt": "2026-11-11T00:00:00Z",
  "notes": {
    "pt-BR": [{ "kind": "feat", "text": "..." }],
    "en": [{ "kind": "feat", "text": "..." }],
    "es": [{ "kind": "feat", "text": "..." }],
    "fr": [{ "kind": "feat", "text": "..." }]
  }
}
```

`product` é `desktop`, `cli` ou `bundle`. `kind` é `feat`, `fix` ou
`security`. Os quatro idiomas são obrigatórios e cada um tem ao menos uma
entrada. Texto vazio não conta.

`changelog/desktop/1.0.18.json` é o espécime do contrato para a versão
instalada do Desktop. Não há asset `desktop-v1.0.18` neste repositório: a
linha `v6.8.x` do monorepo não é esta versão, e um update só existe quando a
tag do produto tem os assets daquele `os/arch`.
