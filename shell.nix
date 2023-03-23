{ pkgs ? (import <nixpkgs> { }).pkgs }:
with pkgs;
mkShell rec {
  packages = [ poetry python3 zlib ta-lib stdenv.cc.cc.lib pkg-config ];

  LD_LIBRARY_PATH = lib.makeLibraryPath packages;
}
