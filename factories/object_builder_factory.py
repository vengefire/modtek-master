from builders.object_builders.DefaultJsonObjectBuilder import DefaultJsonObjectBuilder
from builders.object_builders.PrefabObjectBuilder import PrefabObjectBuilder
from builders.object_builders.asset_bundle_object_builder import AssetBundleObjectBuilder
from data.enums import ObjectType
from factories.base_factory import BaseFactory


class ObjectBuilderFactory(BaseFactory):
    @staticmethod
    def build_from_type(manifest_entry):
        if manifest_entry.object_type == ObjectType.Prefab:
            return PrefabObjectBuilder(manifest_entry)
        elif manifest_entry.object_type == ObjectType.AssetBundle:
            return AssetBundleObjectBuilder(manifest_entry)
        return DefaultJsonObjectBuilder(manifest_entry)
