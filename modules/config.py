import os, sys, logging

log = logging.getLogger('web_api.config')

def get_config(config_filepath, default_db_filepath, default_log_level):
    if not os.path.isfile(config_file):
        log.warning("Could not find config file '{0}'. Creating it there with default values.".format(config_filepath))
        create_default_config(config_filepath, default_db_filepath, default_log_level)
    
    return parse_config(config_filepath, default_db_filepath, default_log_level)
        
        
 
def create_default_config(filepath, default_db_filepath, default_log_level):
    with open(filepath, 'w') as fd:
        fd.write("db_filepath={0}\n".format(default_db_filepath))
        fd.write("log_level={0}\n".format(logging.getLevelName(default_log_level)))

def parse_config(config_filepath, default_db_filepath, default_log_level):
    config = {"db_filepath": default_db_filepath, "log_level": default_log_level}

    with open(config_filepath, 'r') as fd:
        for line_num, line in enumerate(fd.readlines()):
            line_clean = line.split("#", 1)[0].strip() #remove comments and whitespace
            if(line_clean):
                try:
                    key, value = line_clean.split("=")
                    key = key.strip()
                    value = value.strip()
                    if(key in config.keys()):
                        config[key] = value
                    else:
                        raise ValueError("The config paramater {0} isn't supported by this application".format(key))                    

                except ValueError as e:
                    log.error("Could not parse line {0} \"{1}\": {2}".format(line_num, line, e))
        
    return config        
