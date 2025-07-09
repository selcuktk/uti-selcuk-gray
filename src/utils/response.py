
from sdks.novavision.src.helper.package import PackageHelper
from components.SelcukGray.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, SelcukGrayOutputs, SelcukGrayResponse, SelcukGrayExecutor, OutputImage

def build_response(context):
    outputImage = OutputImage(value=context.image)
    Outputs = SelcukGrayOutputs(outputImage=outputImage)
    selcukGrayResponse = SelcukGrayResponse(outputs=Outputs)
    selcukGrayExecutor = SelcukGrayExecutor(value=selcukGrayResponse)
    executor = ConfigExecutor(value=selcukGrayExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
