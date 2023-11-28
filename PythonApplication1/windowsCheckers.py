import windows_tools
import windows_tools.antivirus


def antivirus_check():
    result = windows_tools.antivirus.get_installed_antivirus_software()
    for cock in result:
        print(cock['name'])
        if cock["name"] != "Windows Defender":
            print("u got an antivirus named" , cock["name"])
        else:
            return
        
antivirus_check()
