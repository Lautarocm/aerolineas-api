"use client"

import { Button } from "@nextui-org/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowDownShortWide } from "@fortawesome/free-solid-svg-icons"; 

export function SortCheckbox({sortDisabled, handleSort, sorted}){

	return(
		<Button isDisabled={sortDisabled} onPress={() => handleSort()} size="xs" radius="full" color={sorted ? "primary" : "default"}>
			{<FontAwesomeIcon icon={faArrowDownShortWide} />}
			{sorted ? "On" : "Off"}
		</Button>
	)
}