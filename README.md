# azure-cli-extension-sample
This is a sample project to show how to [author an Azure CLI 2.0 extension](https://github.com/Azure/azure-cli/blob/master/doc/extensions/authoring.md).

## Usages:

1. navigate to the package folder:
```{r, engine = 'bash', eval = FALSE}
    cd helloworldsample
```
2. build python wheel package:
```{r, engine = 'bash', eval = FALSE}
    python3 setup.py bdist_wheel
```
3. add azure cli extension from local file:
```{r, engine = 'bash', eval = FALSE}
    az extension add --source ./dist/helloworldsample-0.0.1-py2.py3-none-any.whl -y
```
4. verify extension worked
```{r, engine = 'bash', eval = FALSE}
    az hello world
```
5. remove azure cli extension
```{r, engine = 'bash', eval = FALSE}
    az extension remove -n "helloworldsample"
```
