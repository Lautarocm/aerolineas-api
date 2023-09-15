"use client"

import styles from "./DefaultMessage.module.css"
import { useContext } from "react"
import { FlightsContext } from "@/app/context/FlightsContext"

export function DefaultMessage(){

    const {offers} = useContext(FlightsContext)

    return(
        <>
            {offers == null ? 
            <span className={styles.defaultMessage}>No hay vuelos</span> :
            (Array.isArray(offers) && offers.length == 0) && <span className={styles.defaultMessage}>Elegí a donde volar</span>}
        </>
    )
}