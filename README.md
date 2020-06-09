# karnak-mainzelliste

This repository is used to overload the default docker image of the mainzelliste.

Further information and documentation on Mainzelliste on the following links:
- [Repository mainzelliste](https://bitbucket.org/medicalinformatics/mainzelliste/src/rc1.8/)
- [Mainzelliste Docker](https://bitbucket.org/medicalinformatics/mainzelliste/src/rc1.8/docker.md)
- [Project web page of the University Medical Center Mainz](https://www.unimedizin-mainz.de/imbei/informatik/ag-verbundforschung/mainzelliste.html?L=1)

## Description

It use a default configuration of mainzelliste used for Karnak.

It add the possibility to read the k1, k2, k3 on environment variables and as a secret. The k1, k2, k3 is additional params for PIDGenerator. PIDGenerate will encrypt the value with the keys k1, k2, k3 and k4 = k1+k2+k3 mod 2^30.

# Docker

Minimum version: **19.03**

The docker image is available on [docker hub](https://hub.docker.com/repository/docker/osirixfoundation/karnak-mainzelliste) named `osirixfoundation/karnak-mainzelliste`.

## Docker build

Launch the following command to build the docker locally:

`docker build -t mainzelliste/locally:latest .`

## Environment variables

`MAINZELLISTE_PID_K1`

The value of the K1 used for the PIDGenerator.

`MAINZELLISTE_PID_K1_FILE`

The value of the K1 used for the PIDGenerator via file input (alternative to `MAINZELLISTE_PID_K1`).

`MAINZELLISTE_PID_K2`

The value of the K2 used for the PIDGenerator.

`MAINZELLISTE_PID_K2_FILE`

The value of the K2 used for the PIDGenerator via file input (alternative to `MAINZELLISTE_PID_K2`).

`MAINZELLISTE_PID_K3`

The value of the K3 used for the PIDGenerator.

`MAINZELLISTE_PID_K3_FILE`

The value of the K3 used for the PIDGenerator via file input (alternative to `MAINZELLISTE_PID_K3`).