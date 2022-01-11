import json
MODULE = 'bcl2fastq'
mi_template_json = {'module_version': '00.00.00', 'program_name': 'bcl2fastq', 'program_subname': '', 'program_version': '2.20.0', 'compute': {'environment': 'aws', 'language': 'Python', 'language_version': '3.7', 'vcpus': 2, 'memory': 6000}, 'program_arguments': '--create-fastq-for-index-reads -R /home/', 'program_input': [{'input_type': 'file', 'input_file_type': 'CSV', 'input_position': -1, 'input_prefix': '--sample-sheet'}], 'program_output': [{'output_type': 'folder', 'output_file_type': '', 'output_position': 0, 'output_prefix': '-o'}], 'alternate_inputs': [], 'alternate_outputs': []}
with open(MODULE+'.template.json','w') as fout:
    json.dump(mi_template_json, fout)

io_json = {'input': ['s3://npipublicinternal/test/bcl/test.samplesheet.csv'], 'output': ['s3://npipublicinternal/test/bcl_out/']\
, 'alternate_inputs': [], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test', 'dryrun': ''} 

with open(MODULE+'_test.io.json','w') as fout:
    json.dump(io_json, fout)
