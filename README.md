# pecl-artifacts

Mirror of the PECL extension tarballs used by Freepik PHP images.

pecl.php.net has no official mirrors and falls over under load. It was unreachable
for most of 2026-10-21, the day of the PHP RCE patch (CVE-2026-109618/109619), while
every image in the company needed a rebuild. PECL is also deprecated upstream in favour
of PIE. Image builds must not depend on it.

Rule: tarballs are committed as-is, byte for byte as published on pecl.php.net. Never
modify or replace one. To upgrade, add the new version next to the old one.

## Packages

| File | SHA256 | Independently verified against |
|---|---|---|
| `packages/grpc-1.84.0.tgz` | `555716233a5cc9a6baa605719f87b7688a88fb8bfdd9b4493396276244d56625` | Content diff vs GitHub `grpc/grpc` tag `v1.84.0` |
| `packages/memcached-3.4.0.tgz` | `c163434eb0da97c8f45c7ad41d979d381f8b81c49402b1b90b063987fb37972e` | Alpine aports `php84-pecl-memcached` sha512 |
| `packages/opentelemetry-1.4.2.tgz` | `a355329259f373c5c7327e66310481726cfabac50cb5483eba000bec791d5017` | Content diff vs GitHub `open-telemetry/opentelemetry-php-instrumentation` tag `1.4.2` |
| `packages/protobuf-5.36.2.tgz` | `f0a17c67de29df0fb0e5215a381df9b155125e1ace6252dd617bf16b4194dd5b` | FreeBSD ports `devel/pecl-protobuf` distinfo |
| `packages/redis-6.3.0.tgz` | `0d5141f634bd1db6c1ddcda053d25ecf2c4fc1c395430d534fd3f8d51dd7f0b5` | Alpine aports `php84-pecl-redis` sha512 |
| `packages/yaml-2.3.0.tgz` | `bc8404807a3a4dc896b310af21a7f8063aa238424ff77f27eb6ffa88b5874b8a` | Alpine aports `php84-pecl-yaml` sha512 |

`SHA256SUMS` is the source of truth. Check a checkout with:

```sh
cd packages && sha256sum -c ../SHA256SUMS
```

## Usage in a Dockerfile

`pecl install` accepts a local tarball and does not touch the network for it
(verified with `--network none` on `php:8.3-fpm-alpine3.23`). Pin the version and
check the hash before installing:

```dockerfile
ARG PECL_MIRROR=https://raw.githubusercontent.com/freepik-company/pecl-artifacts/main/packages

ADD ${PECL_MIRROR}/redis-6.3.0.tgz /tmp/pecl/redis-6.3.0.tgz
RUN echo "0d5141f634bd1db6c1ddcda053d25ecf2c4fc1c395430d534fd3f8d51dd7f0b5  /tmp/pecl/redis-6.3.0.tgz" | sha256sum -c - \
 && pecl install /tmp/pecl/redis-6.3.0.tgz \
 && docker-php-ext-enable redis \
 && rm -rf /tmp/pecl
```

While this repository is private, `ADD` from `raw.githubusercontent.com` needs a token.
Either make the repository public (the content is public open source) or check it out in
the pipeline and `COPY` the tarball from the build context.

## Adding a package

1. Resolve the stable version: `curl https://pecl.php.net/rest/r/<name>/stable.txt`
2. Download: `curl -O https://pecl.php.net/get/<name>-<version>.tgz`
3. Verify against an independent source before committing. In order of preference:
   Alpine aports `community/php8x-pecl-<name>/APKBUILD` (`sha512sums`), FreeBSD ports
   `*/pecl-<name>/distinfo` (`SHA256`), or a file-by-file diff of the extracted tarball
   against the upstream GitHub release tag.
4. Copy it to `packages/`, regenerate `SHA256SUMS` (`cd packages && sha256sum *.tgz > ../SHA256SUMS`)
   and add the row above with what you verified it against.
