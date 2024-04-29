def define_env(env):

   @env.macro
   def mlperf_inference_run_command(spaces, model, implementation, category, scenario):
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
       scenario_option = f"--scenario={scenario}"
 
     return f"\n{f_pre_space} cm run script --tags=run-mlperf,inference{scenario_variation_tag} \\\n {pre_space} --model={model} \\\n {pre_space} --implementation={implementation} \\\n {pre_space} --category={category} \\\n {pre_space} {scenario_option}"
     '''
     return f"\n{f_pre_space}```bash\n{f_pre_space} cm run script --tags=run-mlperf,inference \\\n {pre_space} --model={model} \\\n {pre_space} --implementation={implementation} \\\n {pre_space} --category={category} \\\n {pre_space} --scenario={scenario}\n {pre_space}```"
     '''
