#
# run_program
#
# Template script that runs a command-line program within a Docker container.
#
import os, subprocess, sys
sys.path.append('global_utils/src/')
import module_utils, file_utils

def runProgram():
    # parse run input arguments
    args = module_utils.getRunArgs( )
    
    # create a working directory
    print('Creating working directory')
    DOCKER_DIR = os.getcwd()
    WORKING_DIR = module_utils.generateWorkingDir(args.working_dir)
    os.chdir(WORKING_DIR)
    OUT_DIR = os.path.join(WORKING_DIR, 'module_out')
    os.mkdir(OUT_DIR)
    
    # setup I/O
    print('Setting up I/O')
    run_arguments_file = file_utils.downloadFile(args.run_arguments, WORKING_DIR)
    run_arguments_json = file_utils.loadJSON( run_arguments_file )
    
    # get module template for this docker module
    module_template_path = module_utils.getModuleTemplate( args.module_name )
    module_template_file = file_utils.downloadFile( module_template_path, WORKING_DIR )
    module_template_json = file_utils.loadJSON( module_template_file )
    
    # parse run arguments and create program arguments to be run via command line
    module_instance_json = module_utils.createModuleInstanceJSON( module_template_json, run_arguments_json )
    print(str(module_instance_json))
    remote_output_directory = module_utils.getOutputDirectory( module_instance_json )
    remote_output_file = module_utils.getOutputFile( module_instance_json )
    program_arguments = module_utils.createProgramArguments( module_instance_json, WORKING_DIR, OUT_DIR )  # files will be downloaded here

    # run program - this should run program w arguments via command line on local machine / container
    print('RUNNING PROGRAM...')
    print('CMD: '+str(program_arguments))    
    module_utils.startProgram( program_arguments, file_utils.getFullPath(OUT_DIR, remote_output_file, True) )
    
    # run any other intermediate programs before final output
    # run_subprogram.runSubprograms()
    
    # upload data output files
    print('Uploading output data files...')
    file_utils.uploadFolder(OUT_DIR, remote_output_directory)
    print('DONE!')
    
    return


if __name__ == '__main__':
    runProgram()
