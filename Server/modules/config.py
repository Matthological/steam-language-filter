import os, sys, logging

log = logging.getLogger('web_api.config')
default_config = {
    'db_filepath': os.path.join( os.path.dirname(os.path.realpath(__file__)), "web_api.sql"),
    'log_level': 'DEBUG'
    }
def get_config(config_filepath):
    if not os.path.isfile(config_filepath):
        log.warning("Could not find config file '{0}'. Using default configuation values.".format(config_filepath))
        return default_config
    return parse_config(config_filepath)
        
        
def create_default_config(filepath):
    with open(filepath, 'w') as fd:
        for key, value in default_config.iteritems:
            fd.write("{0}={1}\n".format(key, value))

def parse_config(config_filepath):
    config = {"db_filepath": default_config["db_filepath"], "log_level": default_config["log_level"]}
    with open(config_filepath, 'r') as fd:
        for line_num, line in enumerate(fd.readlines()):
            line_clean = line.split("#", 1)[0].strip() #remove comments and whitespace
            if(line_clean):
                try:
                    key, value = line_clean.split("=")
                    key = key.strip().lower()
                    value = value.strip()
                    
                    if key == "log_level":
                        value = value.upper()
                        supported_levels =  ["INFO", "WARNING", "ERROR", "DEBUG", "NOTSET"]
                        if value not in supported_levels:
                            raise ValueError("Log levels supported are: {0}".format(supported_levels))
                        else:
                            config["log_level"] = value

                    elif key == "db_filepath":
                        config["db_filepath"] = value
                    else:
                       raise ValueError("The config paramater {0} isn't supported by this application".format(key))                    

                except ValueError as e:
                    log.error("Could not parse config line {0} \"{1}\": {2}".format(line_num, line, e))    
    return config        
