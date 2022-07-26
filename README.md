# Hubbard-model-

This project compute the energy eigenvalue of the simple Hubbard Hamiltonian by using exact diagonalization.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to use](#how_to_use)
* [Example](#example)
* [Project status](#project_status)
## General info
This project was done during my 2022 summer intership.
	
## Technologies
Project is created with:
* Python 3.10.4
* Numpy library
* sys library 
	
## How to use
The program take two entry as parameters. First, the number of sites and second, the symmetry group under which you want to symmetrize the Hamiltonian. 
In the command line, it look like this:
python3 hubbard_diag_v5.py number of sites symmetry group
Example, if I wanted the eigenvalue for the two sites Hamiltonian under the C2 symmetry group, it would look like this:
python3 hubbard_diag_v5.py 2 "c2"
The file groups.py contain some of the more common group such that only typing the name as a string of the group under Schonflies convention is enough. 

## What if the group I want to use is not in groups.py ?
You need to add it. Here is how:
First: you need to know how your group permute your sites. For example, 

## Project status
Work in progress.
