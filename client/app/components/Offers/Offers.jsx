"use client"

import { DefaultMessage } from "../DefaultMessage/DefaultMessage"
import styles from "./Offers.module.css"
import { OfferCard } from "../OfferCard/OfferCard"
import { useContext } from "react"
import { FlightsContext } from "@/app/context/FlightsContext"
import { useSortFilter } from "@/app/hooks/useSortFilter"

export function Offers(){
    
    const {offersExist} = useContext(FlightsContext)
    const {offersToShow} = useSortFilter()
    
    return(
        offersExist ?
        <ul className={styles.offers}>
            {offersToShow.map(offer => {
                return (
                    <li key={`${offer["id"]}`}><OfferCard offer={offer}></OfferCard></li>
                )
            })}
        </ul> :
        <DefaultMessage />
    )
}