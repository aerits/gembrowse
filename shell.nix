{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/eabc38219184cc3e04a974fe31857d8e0eac098d.tar.gz") {} }:

pkgs.mkShell {
  packages = [
    pkgs.tmux
    pkgs.python39
    pkgs.python39Packages.pyqt5
    pkgs.python39Packages.setuptools
    pkgs.qt5Full
    pkgs.xwayland
  ];
}
