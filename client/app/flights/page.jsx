"use client"

import styles from "./flights.module.css"
import { Searchbox } from "../components/Searchbox/Searchbox";
import { OffersContainer } from "../components/OffersContainer/OffersContainer";
import FlightsProvider, { FlightsContext } from "../context/FlightsContext";
import { useContext } from "react";

function SearchContainer(){


    const {offersExist} = useContext(FlightsContext)

    return(
        <div className={`${offersExist ? styles.fullHeight : ""} ${styles.searchContainer}`}>
            <Searchbox />
            <OffersContainer />
        </div>
    )
}

export default function Flights(){



    console.log("renderizando padre")

    return(
        <FlightsProvider>
            
            <div className={styles.flightsContainer}>
                <SearchContainer />
            </div>
        </FlightsProvider>
    )
}