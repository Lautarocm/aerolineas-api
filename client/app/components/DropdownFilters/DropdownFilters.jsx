"use client"

import { Button, Dropdown, DropdownTrigger, DropdownMenu, DropdownItem } from "@nextui-org/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFilter } from "@fortawesome/free-solid-svg-icons";
import styles from "./DropdownFilters.module.css"
import flightsStyles from "../../flights/flights.module.css"
import { useFilter } from "@/app/hooks/useFilter";

const monthsArray = [
    {
        key: "01",
        month: "Ene"
    },
    {
        key: "02",
        month: "Feb"
    },
    {
        key: "03",
        month: "Mar"
    },
    {
        key: "04",
        month: "Abr"
    },
    {
        key: "05",
        month: "May"
    },
    {
        key: "06",
        month: "Jun"
    },
    {
        key: "07",
        month: "Jul"
    },
    {
        key: "08",
        month: "Ago"
    },
    {
        key: "09",
        month: "Sep"
    },
    {
        key: "10",
        month: "Oct"
    },
    {
        key: "11",
        month: "Nov"
    },
    {
        key: "12",
        month: "Dic"
    }
]

export function DropdownFilters({className, filterDisabled, filtered}){

    const {months, handleFilter} = useFilter()

    return(
        <Dropdown>
            <DropdownTrigger>
                <Button className={className} color={filtered ? "primary" : "default"} isDisabled={filterDisabled} size="xs" radius="full"><FontAwesomeIcon className="text-stone-400" icon={faFilter} /></Button>
            </DropdownTrigger>
            <DropdownMenu
            className={styles.ddMenu}
            disallowEmptySelection={false}
            aria-label="filtrar por meses"
            closeOnSelect={false}
            selectionMode="multiple"
            variant="faded"
            selectedKeys={months}
            onSelectionChange={handleFilter}>
                {monthsArray.map((month) => (
                    <DropdownItem color="primary"
                    key={month.key}
                    className={styles.ddItem}>
                        {month.month}
                    </DropdownItem>
                ))}
            </DropdownMenu>
        </Dropdown>
    )
}
