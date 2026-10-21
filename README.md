# pecl-artifacts

Mirror of the PECL extension tarballs used by Freepik PHP images.

pecl.php.net has no official mirrors and falls over under load. It was unreachable for
most of 2026-10-21, the day of the PHP RCE patch (CVE-2026-109618/109619), while every
image in the company needed a rebuild. PECL is also deprecated upstream in favour of PIE.
Image builds must not depend on it: install from this repository, pinned and checksummed.

Rules:

- Tarballs are committed byte for byte as published on pecl.php.net. Never modify or
  replace one. To upgrade, add the new version next to the old one.
- Every tarball is verified against an independent source before it is committed
  (see the table). `SHA256SUMS` is the source of truth.

## Packages

Inventory as of 2026-10-21 of every `pecl install` / `install-php-extensions` across
freepik-company repositories: the current stable of each package, every version that is
explicitly pinned somewhere, plus `xdebug-3.1.6` and `memcached-3.2.0` for the images
still on PHP 7.x / 8.0 / 8.1. The PHP range is what each `package.xml` declares.

| File | PHP (declared) | SHA256 | Verified against |
|---|---|---|---|
| `amqp-2.2.0.tgz` | 7.4.0+ | `5ae624bd785e2995…` | Alpine aports sha512, FreeBSD ports sha256, GitHub `php-amqp/php-amqp` v2.2.0 (245/245 files) |
| `apcu-5.1.28.tgz` | 7.0.0-dev+ | `ca9c1820810a1687…` | Alpine aports sha512, FreeBSD ports sha256, GitHub `krakjoe/apcu` v5.1.28 (127/127) |
| `grpc-1.45.0.tgz` | 7.0.0+ | `48f9c408167cd2c5…` | GitHub `grpc/grpc` v1.45.0: every `src/` and `include/` file identical; `third_party/` comes from submodules, not compared |
| `grpc-1.63.0.tgz` | 7.0.0+ | `0d67d0935f1e4a1f…` | GitHub `grpc/grpc` v1.63.0, same method |
| `grpc-1.68.0.tgz` | 7.0.0+ | `4e022e052d5b7997…` | GitHub `grpc/grpc` v1.68.0, same method |
| `grpc-1.84.0.tgz` | 7.0.0+ | `555716233a5cc9a6…` | GitHub `grpc/grpc` v1.84.0, same method |
| `imagick-3.8.1.tgz` | 5.6.0+ | `3a3587c0a524c17d…` | Alpine aports sha512, FreeBSD ports sha256, GitHub `Imagick/imagick` 3.8.1 (only the `PHP_IMAGICK_VERSION` macro is substituted at release) |
| `mcrypt-1.0.3.tgz` | 7.2.0 to 8.0.0 | `affd675843a079e9…` | GitHub `php/pecl-encryption-mcrypt` 1.0.3 (71/71) |
| `mcrypt-1.0.4.tgz` | 7.2.0 to 8.1.0 | `98153e78958d7a48…` | GitHub `php/pecl-encryption-mcrypt` 1.0.4 (59/59) |
| `mcrypt-1.0.9.tgz` | 7.2.0 to 8.6.0 | `2a9ef0817d3bf677…` | GitHub `php/pecl-encryption-mcrypt` 1.0.9 (59/59) |
| `memcache-8.2.tgz` | 8.0.0+ | `b3f0640eacdeb904…` | Alpine aports sha512, FreeBSD ports sha256, GitHub `websupport-sk/pecl-memcache` 8.2 (107/107) |
| `memcached-3.2.0.tgz` | 7.0.0+ | `2a41143a7b29f4a9…` | GitHub `php-memcached-dev/php-memcached` v3.2.0 (130/130) |
| `memcached-3.3.0.tgz` | 7.0.0+ | `2b85bf6699497170…` | GitHub `php-memcached-dev/php-memcached` v3.3.0 (130/130) |
| `memcached-3.4.0.tgz` | 7.0.0+ | `c163434eb0da97c8…` | Alpine aports sha512 |
| `mongodb-2.5.5.tgz` | 8.1.0 to 8.99.99 | `0eaf84ff709f7318…` | GitHub `mongodb/mongo-php-driver` 2.5.5: 2528 files identical, 0 differ; bundled libmongoc/libbson come from submodules, not compared |
| `msgpack-3.0.1.tgz` | 7.0.0+ | `e30be355ab79aaea…` | Alpine aports sha512, FreeBSD ports sha256, GitHub `msgpack/msgpack-php` v3.0.1 (169/169) |
| `opencensus-0.3.0.tgz` | 7.0.0+ | `2e34b8b5c324cf57…` | GitHub `census-instrumentation/opencensus-php` `master`/ext (94/94). Extension 0.3.0 was never tagged upstream; last ext change is from 2021-07-08. Alpha release, what `pecl install opencensus-alpha` resolves to |
| `openswoole-26.2.0.tgz` | 8.3.0+ | `2b411b41e96916cc…` | GitHub `openswoole/ext-openswoole` v26.2.0: 1669 identical, 0 differ, 65 not compared |
| `openswoole-4.11.1.tgz` | 7.4.0+ | `461a1ae27cbce9dc…` | GitHub `openswoole/ext-openswoole` v4.11.1: 2063 identical, 0 differ, 63 generated/submodule files not compared |
| `opentelemetry-1.4.1.tgz` | 8.1.0+ | `981edebd3d01b942…` | GitHub `open-telemetry/opentelemetry-php-instrumentation` 1.4.1/ext (89/89) |
| `opentelemetry-1.4.2.tgz` | 8.1.0+ | `a355329259f373c5…` | GitHub `open-telemetry/opentelemetry-php-instrumentation` 1.4.2/ext (90/90) |
| `pcov-1.0.12.tgz` | 7.1.0+ | `23255c8c9335a963…` | Alpine aports sha512, GitHub `krakjoe/pcov` v1.0.12 (25/25) |
| `protobuf-5.36.2.tgz` | 8.2.0+ | `f0a17c67de29df0f…` | FreeBSD ports sha256 |
| `redis-6.1.0.tgz` | 7.4.0+ | `f10405f639fe415e…` | GitHub `phpredis/phpredis` 6.1.0: 57 identical, 0 differ, 6 generated files not in the tag |
| `redis-6.3.0.tgz` | 7.4.0+ | `0d5141f634bd1db6…` | Alpine aports sha512 |
| `swoole-6.2.3.tgz` | 8.2.0 to 8.5.99 | `21dfa1c4a4a09f4d…` | GitHub `swoole/swoole-src` v6.2.3: every source file identical; the PECL release only normalises `tests/*.phpt` names and adds SKIPIF headers |
| `uv-0.3.0.tgz` | 8.0.0+ | `a11f9c987f4c466b…` | GitHub `amphp/ext-uv` v0.3.0 (99/99) |
| `uv-0.3.1.tgz` | 8.0.0+ | `1b18d961543f76ee…` | FreeBSD ports sha256, GitHub `amphp/ext-uv` v0.3.1 (103/103) |
| `xdebug-2.9.1.tgz` | 7.1.0+ | `f840292e9fd56f51…` | GitHub `xdebug/xdebug` 2.9.1 (94 identical, 0 differ, 2 generated files) |
| `xdebug-3.1.6.tgz` | 7.2.0 to 8.1.99 | `554eca0b4d5b7b93…` | GitHub `xdebug/xdebug` 3.1.6 (100/100) |
| `xdebug-3.3.0.tgz` | 8.0.0 to 8.3.99 | `46f839657ff1c42d…` | GitHub `xdebug/xdebug` 3.3.0 (109/109) |
| `xdebug-3.3.2.tgz` | 8.0.0 to 8.3.99 | `15545b8311bedb5e…` | GitHub `xdebug/xdebug` 3.3.2 (109/109) |
| `xdebug-3.5.3.tgz` | 8.0.0 to 8.5.99 | `f073de91bea04610…` | GitHub `xdebug/xdebug` 3.5.3 (124/124) |
| `xhprof-2.3.10.tgz` | 7.0.0+ | `251aee99c2726ebc…` | GitHub `longxinH/xhprof` v2.3.10 (49/50; only the `XHPROF_VERSION` macro differs, upstream forgot to bump it in the tag) |
| `yaml-2.3.0.tgz` | 7.1.0+ | `bc8404807a3a4dc8…` | Alpine aports sha512 |

Full hashes: `SHA256SUMS`. Check a checkout with:

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

Several packages at once: `ADD` each tarball, run `sha256sum -c` on a file with their
lines, then `pecl install /tmp/pecl/a.tgz /tmp/pecl/b.tgz`.

## Adding a package

1. Resolve the stable version: `curl https://pecl.php.net/rest/r/<name>/stable.txt`
   (`beta.txt` / `alpha.txt` for packages that only ship pre-releases).
2. Download: `curl -O https://pecl.php.net/get/<name>-<version>.tgz`
3. Verify against an independent source before committing. In order of preference:
   Alpine aports `community/php8x-pecl-<name>/APKBUILD` (`sha512sums`, only when its
   `source=` is the PECL tarball and not a GitHub archive), FreeBSD ports
   `*/pecl-<name>/distinfo` (`SHA256`), or a file-by-file comparison of the extracted
   tarball against the upstream GitHub tag. Version-string substitutions in a header
   are normal; any other source difference is a reason not to commit.
4. Copy it to `packages/`, regenerate `SHA256SUMS` (`cd packages && sha256sum *.tgz > ../SHA256SUMS`)
   and add the row above with what you verified it against.
