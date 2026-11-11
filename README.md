# perstein-releases

Catálogo das releases dos produtos baixáveis do Perstein. Este git guarda o
changelog e o índice. O binário, o zip, o instalador e o checksum ficam nos
assets da GitHub Release da tag correspondente. Este repositório não recebe
esses arquivos.

Repositório privado. A API do Perstein, com sessão Cloud, lê a release e
devolve um link temporário do GitHub. A API não envia o arquivo.

## Produtos

| Produto | Tag | Papel |
| --- | --- | --- |
| `desktop` | `desktop-vX.Y.Z` | Update do Perstein Desktop já instalado |
| `cli` | `cli-vX.Y.Z` | Update do binário `perstein` (CLI e MCP) |
| `bundle` | `bundle-vX.Y.Z` | Instalação da suíte (Desktop, CLI e MCP) |

Draft e prerelease não entram no canal estável. Uma tag sem asset do
`os/arch` pedido não é a latest daquele sistema.

## Update e install

- **Update.** A maior tag `desktop-vX.Y.Z` publicada, com asset do mesmo
  `os/arch` do processo, e semver maior que a versão instalada. O asset é o
  pacote daquele produto, não o bundle.
- **Install.** A maior tag `bundle-vX.Y.Z` com o instalador daquele `os/arch`.
  Não se compara com a versão do Desktop.

A linha `v6.8.x` do monorepo `moreirawebmaster/perstein` é a plataforma. Ela
não é versão de Desktop, CLI nem bundle.

## Assets

Nome:

```text
perstein-<produto>_<versão>_<os>_<arch>.<ext>
perstein-<produto>_<versão>_<os>_<arch>.<ext>.sha256
perstein-<produto>_<versão>_<os>_<arch>.<ext>.sig
```

`os` é `darwin`, `windows` ou `linux`. `arch` é `amd64` ou `arm64`.

| Produto | darwin | windows | linux |
| --- | --- | --- | --- |
| desktop | `.dmg` | `.msi` | `.tar.gz` |
| cli | `.tar.gz` | `.zip` | `.tar.gz` |
| bundle | `.pkg` | `.msi` | `.deb` e `.rpm` |

Linux do bundle tem dois assets no mesmo `os/arch`, distinguidos pela
extensão. Os outros pares produto/`os`/`arch` têm um asset.

Release sem os quatro idiomas do changelog, sem `.sha256` ou sem `.sig` de
cada asset não é publicada. O corpo da release é renderizado do JSON. O JSON
é a fonte.

## Changelog

`changelog/<produto>/<versão>.json`, no mesmo commit da tag. O índice
`index.json` lista as versões que têm changelog neste git. Presença no índice
não significa que existe asset para baixar.
