"use client"

import { Button } from "@nextui-org/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowDownShortWide } from "@fortawesome/free-solid-svg-icons"; 
import { useSort } from "@/app/hooks/useSort";

export function SortCheckbox({sortDisabled}){

	const {sorted, handleSort} = useSort()

	return(
		<Button isDisabled={sortDisabled} onPress={() => handleSort()} size="xs" radius="full" color={sorted ? "primary" : "default"}>
			{<FontAwesomeIcon icon={faArrowDownShortWide} />}
			{sorted ? "On" : "Off"}
		</Button>
	)
}