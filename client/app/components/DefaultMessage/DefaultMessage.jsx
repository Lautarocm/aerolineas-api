"use client"

import styles from "./DefaultMessage.module.css"
import { useContext } from "react"
import { FlightsContext } from "@/app/context/FlightsContext"

export function DefaultMessage(){

    const {offers} = useContext(FlightsContext)

    return(
        <>
            {offers == [] && <span className={styles.defaultMessage}>Elegí a donde volar</span>}
            {offers == null && <span className={styles.defaultMessage}>No hay vuelos</span>}
        </>
    )
}