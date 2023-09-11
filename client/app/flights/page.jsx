"use client"

import styles from "./flights.module.css"
import { useEffect, useState } from "react";
import { Button, Select, SelectSection, SelectItem, Avatar, Spinner } from "@nextui-org/react";
import OfferCard from "../components/OfferCard/OfferCard"
import DropdownFilters from "../components/DropdownFilters/DropdownFilters"
import SortCheckbox from "../components/SortCheckbox/SortCheckbox"
import { getAirports } from "../services/airports";
import { getOffers } from "../services/offers";
import iguazu from "../../../data/iguazu.json" assert {type: "json"}

export default function Flights(){

    const [airports, setAirports] = useState([])
    const [origin, setOrigin] = useState("")
    const [destination, setDestination] = useState("")
    const [loading, setLoading] = useState(false)
    const [offers, setOffers] = useState([])
    const [offersExist, setOffersExist] = useState(false)
    const [months, setMonths] = useState([])
    const [searchDisabled, setSearchDisabled] = useState(true)
    const [offersToShow, setOffersToShow] = useState([])
    const [isSorted, setIsSorted] = useState(false)
    const [isFiltered, setIsFiltered] = useState(false)
    const [resetChildState, setResetChildState] = useState(false)
    const [countries, setCountries] = useState([])

    const handleSearch = () => {
        
        const queryParams = []
        origin != "" && queryParams.push(`origin=${origin}`)
        destination != "" && queryParams.push(`destination=${destination}`)
        const query = queryParams.join("&")
        const url = `http://localhost:8080/scrape?${query}`

        setResetChildState(true)
        setMonths([])
        setIsSorted(false)
        setIsFiltered(false)
        setOffersExist(false)
        setLoading(true)
        getOffers(url).then(setOffers).finally(() => setLoading(false))
    }

    const sortOffers = (offers) => {
        const sortedOffers = offers.slice().sort((a, b)=>a["price"]-b["price"])
        return sortedOffers
    }

    const filterOffers = (offers) => {
        const filteredOffers = offers.filter(offer => {
            return months.has(offer.departures[0].split("-")[1])
        })
        return filteredOffers
    }

    const handleSort = (isOn) => {
        setIsSorted(isOn)
    }

    const handleFilter = (months) => {
        if(months.size > 0){
            setIsFiltered(true)
            setMonths(months)
            
        }
        else{setIsFiltered(false)}
    }

    const sortAndFilter = (offers) => {
        if(isSorted && isFiltered){
            const filteredOffers = filterOffers(offers)
            const sortedOffers = sortOffers(filteredOffers)
            setOffersToShow(sortedOffers)
        }
        else if(isFiltered && !isSorted){
            const filteredOffers = filterOffers(offers)
            setOffersToShow(filteredOffers)
        }
        else if(isSorted && !isFiltered){
            const sortedOffers = sortOffers(offers)
            setOffersToShow(sortedOffers)
        }
        else{
            setOffersToShow(offers)
        }
    }

    const getCountries = () => {
        const countries = []
        airports.forEach(airport => {
            const countryName = airport.city.country.name
            if (!countries.includes(countryName))
            countries.push(countryName)
        });
        setCountries(countries)
    }

    useEffect(() => {
        getAirports().then(setAirports)
    }, [])

    // useEffect para hacer pruebas si me banean la ip
    // useEffect(() => {
    //     setOffers(iguazu)
    //     setOffersExist(true)
    // })

    // habilitar boton buscar solo si se eligió origen y destino
    useEffect(() => {
        if(origin && destination){
            setSearchDisabled(false)
        }
        else{setSearchDisabled(true)}
    }, [origin, destination])

    // verificar que haya ofertas
    useEffect(() => {
        if(Array.isArray(offers)){
            offers.length > 0 && setOffersExist(true)
        }
    }, [offers])

    useEffect(() => {
        offersExist && sortAndFilter(offers)
    }, [offers, isSorted, isFiltered, months, offersExist])

    useEffect(() => {
        getCountries()
    },[airports])

    return(
        
        <div className={styles.flightsContainer}>
            <div className={`${offersExist ? styles.fullHeight : ""} ${styles.searchContainer}`}>
                <div className={styles.filtersContainer}>
                    <Select
                    className={styles.select}
                    onChange={e => setOrigin(e.target.value)}
                    radius="sm"
                    variant="flat"
                    size="sm"
                    label="Origen"
                    color="primary"
                    items={airports}>
                        {countries.map(country => 
                            <SelectSection key={country} showDivider title={country}>
                                {airports.map(airport => 
                                    airport.city.country.name == country &&
                                    <SelectItem
                                    startContent={<Avatar alt={`${airport.city.country.name}`} className="w-6 h-6" src={`https://flagcdn.com/${airport.city.country.code.toLowerCase()}.svg`} />}
                                    key={airport.iataCode}
                                    value={airport.iataCode}
                                    color="primary">
                                        {`${airport.city.name} (${airport.iataCode})`}
                                    </SelectItem>
                                )}
                            </SelectSection>
                        )}
                    </Select>
                    <Select
                    className={styles.select}
                    onChange={e => setDestination(e.target.value.toUpperCase())}
                    radius="sm"
                    variant="flat"
                    size="sm"
                    label="Destino"
                    color="primary"
                    items={airports}>
                    {countries.map(country => 
                        <SelectSection key={country} showDivider title={country}>
                            {airports.map(airport => 
                                airport.city.country.name == country &&
                                <SelectItem
                                startContent={<Avatar alt={`${airport.city.country.name}`} className="w-6 h-6" src={`https://flagcdn.com/${airport.city.country.code.toLowerCase()}.svg`} />}
                                key={airport.iataCode}
                                value={airport.iataCode}
                                color="primary">
                                    {`${airport.city.name} (${airport.iataCode})`}
                                </SelectItem>
                            )}
                        </SelectSection>
                    )}
                    </Select>
                    <div className={styles.searchButtons}>
                        <Button
                        className={styles.button}
                        onClick={handleSearch}
                        color="primary"
                        size="md"
                        radius="md"
                        isDisabled={searchDisabled}
                        >
                            Buscar
                        </Button>
                        <SortCheckbox resetState={resetChildState} onResetComplete={() => setResetChildState(false)} sortDisabled={!offersExist} handleSort={handleSort} />
                        <DropdownFilters resetState={resetChildState} onResetComplete={() => setResetChildState(false)} filterDisabled={!offersExist} handleFilter={handleFilter} />
                    </div>
                </div>
                <div className={styles.offersContainer}>
                    {
                    loading ? 
                    <Spinner /> :
                        offersExist ? 
                            <ul className={styles.offers}>
                                    {offersToShow.map(offer => 
                                        <li key={offer.id}><OfferCard offer={offer}></OfferCard></li> 
                                    )}
                            </ul> : 
                            offers ?
                                <span className={styles.defaultText}>Elegí a donde volar</span> :
                                <span className={styles.defaultText}>No hay vuelos</span>
                    }
                </div>
            </div>
        </div>  
    )
}