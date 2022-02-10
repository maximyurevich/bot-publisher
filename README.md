# Telegram publisher bot
This is telegram broadcaster bot based on aiogram

![Screenshot](Screenshot-2022-02-10-110555.jpg)

For launching on any OS you should set ENVPATH on VSCode launch.json for debugging purposes

```json
{
    "configurations": [
        {
            "name": "Python: Текущий файл",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "ENVPATH": "${workspaceRoot}/.env.development"
            }
        }
    ]
}
```


