import json
MODULE = 'bcl2fastq'
mi_template_json = {'module_version': '00.00.00', 'program_name': 'bcl2fastq', 'program_subname': '', 'program_version': '2.20.0', 'compute': {'environment': 'aws', 'language': 'Python', 'language_version': '3.7', 'vcpus': 2, 'memory': 6000}, 'program_arguments': '--create-fastq-for-index-reads', 'program_input': [{'input_type': 'folder', 'input_file_type': '', 'input_position': -1, 'input_prefix': '-R'}], 'program_output': [{'output_type': 'folder', 'output_file_type': '', 'output_position': 0, 'output_prefix': '-o'}], 'alternate_inputs': [{'input_type': 'file', 'input_file_type': 'CSV', 'input_position': -1, 'input_prefix': '--sample-sheet'}], 'alternate_outputs': []}
with open(MODULE+'.template.json','w') as fout:
    json.dump(mi_template_json, fout)

io_dryrun_json = {'input': ['s3://npipublicinternal/test/bcl/'], 'output': ['s3://npipublicinternal/test/bcl_out/'], 'alternate_inputs': [], 'alternate_outputs': ['s3://npipublicinternal/test/bcl/test.samplesheet.csv'], 'program_arguments': '', 'sample_id': MODULE+'_test', 'dryrun': ''}
io_json = {'input': ['s3://npipublicinternal/test/bcl/'], 'output': ['s3://npipublicinternal/test/bcl_out/'], 'alternate_inputs': ['s3://npipublicinternal/test/bcl/test.samplesheet.csv'], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test'} 

with open(MODULE+'.dryrun_test.io.json','w') as fout:
    json.dump(io_dryrun_json, fout)
with open(MODULE+'.test.io.json','w') as fout:
    json.dump(io_json, fout)    
