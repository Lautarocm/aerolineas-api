"use client"

import { Select, SelectSection, SelectItem, Avatar } from "@nextui-org/react"
import { useAirports } from "@/app/hooks/useAirports"
import { useCountries } from "@/app/hooks/useCountries"

export function CustomSelect({className, onChange, label}){

    const {airports} = useAirports()
    const {countries} = useCountries(airports)
    
    return(
        <Select
        className={className}
        onChange={e => onChange(e.target.value)}
        radius="sm"
        variant="flat"
        size="sm"
        label={label}
        color="primary"
        items={airports}>
            {countries.map(country => 
                <SelectSection key={country} showDivider title={country}>
                    {airports.map(airport => 
                        airport.city.country.name === country &&
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
    )
}