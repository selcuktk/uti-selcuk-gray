from sdks.novavision.src.helper.package import PackageHelper
from components.SelcukGray.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, SelcukGrayExecutorOutputs, SelcukGrayExecutorResponse, SelcukGrayExecutor, OutputImage

def build_response(context):
    outputImage = OutputImage(value=context.image)
    selcukGrayExecutorOutputs = SelcukGrayExecutorOutputs(outputImage=outputImage)
    selcukGrayExecutorResponse = SelcukGrayExecutorResponse(outputs=selcukGrayExecutorOutputs)
    selcukGrayExecutor = SelcukGrayExecutor(value=selcukGrayExecutorResponse)
    executor = ConfigExecutor(value=selcukGrayExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
