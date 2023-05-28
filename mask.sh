#!/bin/bash

DWI=$1
CFA=$2

#compute brain mask
bet $DWI bet -R -m -f 0.3

#erode mask of 2 voxels
fslmaths bet_mask.nii.gz -ero bet_mask1.nii.gz
fslmaths bet_mask1.nii.gz -ero bet_mask2.nii.gz

#apply brain mask to CFA
fslmaths $CFA -mas bet_mask2.nii.gz cfa_masked.nii.gz

