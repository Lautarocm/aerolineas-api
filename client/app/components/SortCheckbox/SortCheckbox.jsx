import { useEffect, useState } from "react";
import styles from "../../flights/flights.module.css"
import { Button } from "@nextui-org/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowDownShortWide } from "@fortawesome/free-solid-svg-icons"; 

export default function Checkbox({handleSort, sortDisabled, resetState, onResetComplete}){

	const [sortOn, setSortOn] = useState(false)

	const handleClick = () => {
		setSortOn((state) => {
			handleSort(!state)
			return !state
		})
	}

    useEffect(() => {
        if(resetState){
            setSortOn(false)
            onResetComplete()
        }
    }, [resetState])

	return(
		<Button isDisabled={sortDisabled} className={styles.sort} onPress={() => handleClick()} size="xs" radius="full" color={sortOn ? "primary" : "default"}>
			{<FontAwesomeIcon icon={faArrowDownShortWide} />}
			{sortOn ? "On" : "Off"}
		</Button>
	)
}