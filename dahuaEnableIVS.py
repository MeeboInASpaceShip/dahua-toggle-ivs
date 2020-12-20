#!/usr/bin/python3
import requests
from requests.auth import HTTPDigestAuth
import re

# SYNTAX FOR SETTING OPTIONS
# http://<ip>/cgi-bin/configManager.cgi?action=setConfig&<paramName>=<paramValue>[&<paramName>=<paramValue>...]

# SHOW ALL VideoAnalyseRules IN BROWSER
# http://<ip>/cgi-bin/configManager.cgi?action=getConfig&name=VideoAnalyseRule

# IVS rules to enable/disable - must EXACTLY match the rule names in the camera
ruleNameList = ['Loitering', 'IVS-1', 'IVS-2', 'IVS-3']

# Get all VideoAnalyseRules (IVS rules) from camera
response = requests.get(
    'http://192.168.1.108/cgi-bin/configManager.cgi',
    params={
        'action': 'getConfig',
        'name': 'VideoAnalyseRule',
        },
    auth=HTTPDigestAuth('admin', 'PASSWORD'),
    )

# Disable each rule
for line in response.text.splitlines():
    for ruleName in ruleNameList:
        #print('Looking for ', ruleName)
        if re.search(ruleName, line):
            ruleLine = line.split('.')
            ruleId = ruleLine[1]

            #print('Line is', line)
            #print('Matched {ruleName} with {ruleId}'.format(ruleName=ruleName, ruleId=ruleId))
            print('Setting {ruleId}.Enable ({ruleName}) to true'.format(ruleId=ruleId,ruleName=ruleName))

            enableRuleId = ruleId + '.Enable'
            #print('enableRuleId =', enableRuleId)

            enableRuleResponse = requests.get(
                    'http://192.168.1.108/cgi-bin/configManager.cgi',
                    params={
                        'action': 'setConfig',
                        enableRuleId: 'true',
                        },
                    auth=HTTPDigestAuth('admin', 'PASSWORD'),
                    )
            print('IPC response was:', enableRuleResponse.status_code)
