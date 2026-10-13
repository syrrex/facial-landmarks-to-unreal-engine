// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class LiveLink_RPM : ModuleRules
{
	public LiveLink_RPM(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "HeadMountedDisplay" });
	}
}
