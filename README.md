# Hubbard-model-

This project compute the energy eigenvalue of the simple Hubbard Hamiltonian by using exact diagonalization.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to use](#how-to-use)
* [The group I want is not in groups.py ?](#the-group-i-want-is-not-in-groups.py-?)
* [Interraction matrix](#interraction-matrix)
* [Example of use](#example-of-use)
* [Inspiration](#inspiration)
* [Project status](#project-status)
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
```
$ python3 hubbard_diag_v5.py 2 "c2"
```
The file groups.py contain some of the more common groups such that only typing the name as a string of the group under Schonflies convention is enough. 

## The group I want is not in groups.py ?
You need to add it. Here is how:

You need to know how your group permute your sites. 

For example, the group c2 for 3 sites is symmetric under reflection of site 0 and site 1 along the axis of site 2. 
Hence, the initial configuration [0,1,2] after c2 reflexion is now [1,0,2]. The latter list is the symmetry generator that you have to add to the function group_create in groups.py as sym_gen. 

Here, sym_gen is a list of lists because we can combine multiple symmetry generators to make more complicate groups. For exemple, we can create the non-abelian group d3 by combining the c2 symmetry generator [1,0,2] with c3 symmetry generator [2,0,1]:
```
def group_create(Nsites,group):
       if Nsites == 3 and group == "d3":
           sym_gen = [[1,0,2],[2,0,1]]
           char_table = [[1,1,1,1,1,1],
                         [1,-1,1,-1,1,-1],
                         [2,0,-1,0,-1,0]]

```
As you see, you also need to give the character table of the group. Ultimately, it would be cool if the program could generate the character table only from the symmetry generator, but for now we have to write it ourself. Also, it is important that the characters fit the group element order. 

## Example of use
So I want to know the eigenvalues of the 3 sites Hubbard Hamiltonian... 


## Interraction matrix
The program suppose that all the sites are interracting with each other. However, if this is not the case, you can write an interraction matrix.
For a 4 sites square system where there is no interraction between diagonals the interraction matrix would be as follow:
```
interaction_matrix = [[0,1,0,1],   (the zeroth sites does not interract with itself and with the second sites hence the 0 in the first row of matrix)
                      [1,0,1,0],   (Same pattern in other rows)
                      [0,1,0,1],
                      [1,0,1,0]]
```
## Inspiration


## Project status
Work in progress. Some changes as to be made to better suit non-abelian groups. 
