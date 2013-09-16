# -*- coding: utf8 -*- 
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class UKFTractographyInputSpec(CommandLineInputSpec):
    dwiFile = File(desc="Input DWI volume", exists=True, argstr="--dwiFile %s")
    seedsFile = File(desc="Seeds for diffusion. If not specified, full brain tractography will be performed, and the algorithm will start from every voxel in the brain mask where the Generalized Anisotropy is bigger than 0.18", exists=True, argstr="--seedsFile %s")
    labels = InputMultiPath(traits.Int, desc="A vector of the ROI labels to be used", sep=",", argstr="--labels %s")
    maskFile = File(desc="Mask for diffusion tractography", exists=True, argstr="--maskFile %s")
    tracts = traits.Either(traits.Bool, File(), hash_files=False, desc="Tracts generated, with first tensor output", argstr="--tracts %s")
    tractsWithSecondTensor = traits.Either(traits.Bool, File(), hash_files=False, desc="Tracts generated, with second tensor output (if there is one)", argstr="--tractsWithSecondTensor %s")
    writeBinaryTracts = traits.Bool(desc="Write tract file as a VTK binary data file", argstr="--writeBinaryTracts ")
    seedsPerVoxel = traits.Int(desc="Number of seeds per voxel", argstr="--seedsPerVoxel %d")
    numTensor = traits.Enum("1", "2", "3", desc="Number of tensors used", argstr="--numTensor %s")
    simpleTensorModel = traits.Bool(desc="Whether to use the simple tensor model. If unchecked, use the full tensor model", argstr="--simpleTensorModel ")
    freeWater = traits.Bool(desc="Adds a term for free water difusion to the model. If checked, the 1T simple model is forced.", argstr="--freeWater ")
    minFA = traits.Float(desc="Abort the tractography when the Fractional Anisotropy is less than this value", argstr="--minFA %f")
    minGA = traits.Float(desc="Abort the tractography when the Generalized Anisotropy is less than this value", argstr="--minGA %f")
    recordFA = traits.Bool(desc="Whether to store FA. Attaches field 'FA', and 'FA2' for 2-tensor case to fiber. ", argstr="--recordFA ")
    recordNMSE = traits.Bool(desc="Whether to store NMSE. Attaches field 'NMSE' to fiber. ", argstr="--recordNMSE ")
    recordTrace = traits.Bool(desc="Whether to store Trace. Attaches field 'Trace', and 'Trace2' for 2-tensor case to fiber.", argstr="--recordTrace ")
    recordFreeWater = traits.Bool(desc="Whether to store the fraction of free water. Attaches field 'FreeWater' to fiber.", argstr="--recordFreeWater ")
    recordState = traits.Bool(desc="Whether to attach the states to the fiber. Will generate field 'state'.", argstr="--recordState ")
    recordCovariance = traits.Bool(desc="Whether to store the covariance. Will generate field 'covariance' in fiber.", argstr="--recordCovariance ")
    recordTensors = traits.Bool(desc="Recording the tensors enables Slicer to color the fiber bundles by FA, orientation, and so on. The fields will be called 'TensorN', where N is the tensor number. ", argstr="--recordTensors ")
    numThreads = traits.Int(desc="Number of threads used during computation. Set to the number of cores on your workstation for optimal speed. If left undefined the number of cores detected will be used. ", argstr="--numThreads %d")
    normalizedDWIData = traits.Bool(desc="Whether the DWI input data is already normalized", argstr="--normalizedDWIData ")
    stepLength = traits.Float(desc="Step length of tractography, in millimeters", argstr="--stepLength %f")
    weightsOnTensors = InputMultiPath(traits.Float, desc="Weights on different tensors when using multiple tensors. There must be one weight for each tensor, and the weights must sum up to 1. Default to equally weighted", sep=",", argstr="--weightsOnTensors %s")
    maxHalfFiberLength = traits.Float(desc="The max length limit of the half fibers generated during tractography. Here the fiber is \'half\' because the tractography goes in only one direction from one seed point at a time", argstr="--maxHalfFiberLength %f")
    seedFALimit = traits.Float(desc="Seed points whose FA are below this value are excluded", argstr="--seedFALimit %f")
    Qm = traits.Float(desc="Process noise for angles/direction", argstr="--Qm %f")
    Ql = traits.Float(desc="Process noise for eigenvalues", argstr="--Ql %f")
    Qw = traits.Float(desc="Process noise for free water weights, ignored if no free water estimation", argstr="--Qw %f")
    Rs = traits.Float(desc="Measurement noise", argstr="--Rs %f")
    maxBranchingAngle = traits.Float(desc="Maximum branching angle, in degrees. When using multiple tensors, a new branch will be created when the tensors' major directions form an angle between (minBranchingAngle, maxBranchingAngle). Branching is supressed when this maxBranchingAngle is set to 0.0", argstr="--maxBranchingAngle %f")
    minBranchingAngle = traits.Float(desc="Minimum branching angle, in degrees. When using multiple tensors, a new branch will be created when the tensors' major directions form an angle between (minBranchingAngle, maxBranchingAngle)", argstr="--minBranchingAngle %f")
    noTransformPosition = traits.Bool(desc="Don't transform Points back from ijk->RAS when writing the output fiber", argstr="--noTransformPosition ")
    branchesOnly = traits.Bool(desc="Only output branches, ignore the primary tracts", argstr="--branchesOnly ")
    storeGlyphs = traits.Bool(desc="Store tensors' main directions as two-point lines in a separate file named glyphs_{tracts}. When using multiple tensors, only the major tensors' main directions are stored", argstr="--storeGlyphs ")
    outputNormalizedDWIData = traits.Bool(desc="Whether to output the normalized DWI data", argstr="--outputNormalizedDWIData ")


class UKFTractographyOutputSpec(TraitedSpec):
    tracts = File(desc="Tracts generated, with first tensor output", exists=True)
    tractsWithSecondTensor = File(desc="Tracts generated, with second tensor output (if there is one)", exists=True)


class UKFTractography(SEMLikeCommandLine):
    """title: 
    UKF Tractography
  

category: 
    Diffusion.Tractography
  

description: 
    This module traces fibers in a DWI Volume using the multiple tensor unscented Kalman Filter methology. For more informations check the documentation.
  

version: 1.0

documentation-url: http://www.nitrc.org/plugins/mwiki/index.php/ukftractography:MainPage

contributor: Yogesh Rathi, Stefan Lienhard, Yinpeng Li, Martin Styner, Ipek Oguz, Yundi Shi, Christian Baumgartner

"""

    input_spec = UKFTractographyInputSpec
    output_spec = UKFTractographyOutputSpec
    _cmd = " UKFTractography "
    _outputs_filenames = {'tracts':'tracts.vtk','tractsWithSecondTensor':'tractsWithSecondTensor.vtk'}
