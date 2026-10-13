// Copyright Epic Games, Inc. All Rights Reserved.

#include "LiveLink_RPMGameMode.h"
#include "LiveLink_RPMCharacter.h"
#include "UObject/ConstructorHelpers.h"

ALiveLink_RPMGameMode::ALiveLink_RPMGameMode()
{
	// set default pawn class to our Blueprinted character
	static ConstructorHelpers::FClassFinder<APawn> PlayerPawnBPClass(TEXT("/Game/ThirdPersonCPP/Blueprints/ThirdPersonCharacter"));
	if (PlayerPawnBPClass.Class != NULL)
	{
		DefaultPawnClass = PlayerPawnBPClass.Class;
	}
}
