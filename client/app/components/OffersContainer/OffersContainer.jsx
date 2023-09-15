"use client"

import { Spinner } from "@nextui-org/react"
import { Offers } from "../Offers/Offers"
import styles from "./OffersContainer.module.css"
import { useContext } from "react"
import { FlightsContext } from "@/app/context/FlightsContext"

export function OffersContainer(){

    const {loading} = useContext(FlightsContext)


    return(
        <div className={styles.offersContainer}>
            {
            loading ? 
            <Spinner />: 
            <Offers />
            }
        </div>
    )
}