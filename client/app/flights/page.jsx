"use client"

import styles from "./flights.module.css"
import { Searchbox } from "../components/Searchbox/Searchbox";
import { OffersContainer } from "../components/OffersContainer/OffersContainer";
import { useSearch } from "../hooks/useSearch";
import { useSelect } from "../hooks/useSelect";
import FlightsProvider from "../context/FlightsContext";

export default function Flights(){

    const {origin, destination} = useSelect()
    const {offersExist} = useSearch(origin, destination)

    return(
        <FlightsProvider>
            <div className={styles.flightsContainer}>
                <div className={`${offersExist ? styles.fullHeight : ""} ${styles.searchContainer}`}>
                    <Searchbox />
                    <OffersContainer />
                </div>
            </div>
        </FlightsProvider>
    )
}