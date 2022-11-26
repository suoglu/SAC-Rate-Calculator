# SAC Rate Calculator

## Contents of Readme

1. About
2. Usage
   1. Description
   2. Arguments
3. Calculation
4. Dependencies

[![Repo on GitLab](https://img.shields.io/badge/repo-GitLab-6C488A.svg)](https://gitlab.com/suoglu/sac-rate-calculator)
[![Repo on GitHub](https://img.shields.io/badge/repo-GitHub-3D76C2.svg)](https://github.com/suoglu/SAC-Rate-Calculator)

---

## About

This repository contains python3 script, [SACcalc.py](Sources/SACcalc.py), for surface air consumption rate calculation.

## Usage

### Description

Run the script and fill the required information. Tool will calculate surface air consumption rate with the unit of volume per minute at sea level. Entering multiple tanks is supported.

### Arguments

It is possible to change the behavior of this tool via calling it with options. List of available options can be found below:

|      Option       | Description                                                                                |
|:-----------------:|--------------------------------------------------------------------------------------------|
|       `-i`        | Use imperial unit (Practically this only changes the depth value for 1 ATM water pressure) |
|       `-h`        | Also ask hours for dive time                                                               |

## Calculation

Total consumed air volume is calculated as sum of _(Start pressure - End pressure) * Tank Volume_ for all tanks.

Total dive time is processed in seconds.

Average pressure is calculated as _Average Pressure = 1 + Average Depth / Water Depth for 1 ATM Water Pressure_

The height of water column that causes 1 ATM is taken 10.3 m (or 33.8 ft).

SAC rate calculated as _Surface Air Consumption Rate = Total Consumed Air Volume * 60 / (Average Pressure * Dive Time in Seconds)_ Volume per Minute at 1 ATM

## Dependencies

Script [SACcalc.py](Sources/SACcalc.py) uses _sys_ module.

Tested on

- Python 3.10.6 on Pop!_OS 22.04 LTS
