def define_env(env):

   @env.macro
   def mlperf_inference_run_command(spaces, model, implementation, framework, category, scenario, device="cpu", execution_mode="test", test_query_count="20"):
     pre_space = ""
     for i in range(1,spaces):
       pre_space  = pre_space + " "
     f_pre_space = pre_space
     pre_space += "  "

     if scenario == "All Scenarios":
       scenario_variation_tag = ",_all_scenarios"
       scenario_option = ""
     else:
       scenario_variation_tag = ""
       scenario_option = f"\\\n {pre_space} --scenario={scenario}"

     cmd_suffix = "" 
     if execution_mode == "test":
       cmd_suffix += f" \\\n {pre_space} --test_query_count={test_query_count}"

     return f"\n{f_pre_space} cm run script --tags=run-mlperf,inference{scenario_variation_tag} \\\n {pre_space} --model={model} \\\n {pre_space} --implementation={implementation} \\\n {pre_space} --framework={framework} \\\n {pre_space} --category={category} \\\n {pre_space} --execution_mode={execution_mode} \\\n {pre_space} --device={device} {cmd_suffix}"
     '''
     return f"\n{f_pre_space}```bash\n{f_pre_space} cm run script --tags=run-mlperf,inference \\\n {pre_space} --model={model} \\\n {pre_space} --implementation={implementation} \\\n {pre_space} --category={category} \\\n {pre_space} --scenario={scenario}\n {pre_space}```"
     '''
