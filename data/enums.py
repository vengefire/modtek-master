from enum import Enum


class ObjectType(Enum):
    AbilityDef = 'AbilityDef'
    AdvancedJSONMerge = 'AdvancedJSONMerge'
    AmmunitionBoxDef = 'AmmunitionBoxDef'
    AmmunitionDef = 'AmmunitionDef'
    AssetBundle = 'AssetBundle'
    CCCategories = 'CCCategories'
    CCDefaults = 'CCDefaults'
    CCTagRestrictions = 'CCTagRestrictions'
    ChassisDef = 'ChassisDef'
    ContractOverride = 'ContractOverride'
    DesignMaskDef = 'DesignMaskDef'
    HardpointDataDef = 'HardpointDataDef'
    HeatSinkDef = 'HeatSinkDef'
    ItemCollectionDef = 'ItemCollectionDef'
    LanceDef = 'LanceDef'
    MEBonusDescriptions = 'MEBonusDescriptions'
    MECriticalEffects = 'MECriticalEffects'
    MechDef = 'MechDef'
    MovementCapabilitiesDef = 'MovementCapabilitiesDef'
    PathingCapabilitiesDef = 'PathingCapabilitiesDef'
    Prefab = 'Prefab'
    SimGameEventDef = 'SimGameEventDef'
    SimGameMilestoneSet = 'SimGameMilestoneSet'
    Sprite = 'Sprite'
    Texture2D = 'Texture2D'
    TurretChassisDef = 'TurretChassisDef'
    TurretDef = 'TurretDef'
    UpgradeDef = 'UpgradeDef'
    VehicleChassisDef = 'VehicleChassisDef'
    VehicleDef = 'VehicleDef'
    WeaponDef = 'WeaponDef'


class ManifestEntryCategory(Enum):
    GameObject = 1
    ModTekInstruction = 2


ModTekInstructionObjects = [ObjectType.AdvancedJSONMerge]
