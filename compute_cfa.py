# Copyright (c) 2023 brainlife.io
#
# This file is a template for a python-based brainlife.io App
# brainlife stages this git repo, writes `config.json` and execute this script.
# this script reads the `config.json` and execute pynets container through singularity
#
# you can run this script(main) without any parameter to test how this App will run outside brainlife
# you will need to copy config.json.brainlife-sample to config.json before running `main` as `main`
# will read all parameters from config.json
#
# Author: Giulia Bertò
# The University of Texas at Austin

from dipy.io.image import load_nifti, save_nifti
from dipy.io import read_bvals_bvecs
from dipy.core.gradients import gradient_table
from dipy.reconst.dti import TensorModel

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-dwi', nargs='?', const=1, default='',
	                    help='dwi')   
    parser.add_argument('-bvals', nargs='?', const=1, default='',
	                    help='bvals') 
    parser.add_argument('-bvecs', nargs='?', const=1, default='',
	                    help='bvecs')  
    args = parser.parse_args()

    data, affine = load_nifti(args.dwi)
    bvals, bvecs = read_bvals_bvecs(args.bvals, args.bvecs)
    gtab = gradient_table(args.bvals, args.bvecs)

    tenmodel = TensorModel(gtab)
    tenfit = tenmodel.fit(data)

    save_nifti('outupt/peaks.nii.gz', tenfit.color_fa, affine)

