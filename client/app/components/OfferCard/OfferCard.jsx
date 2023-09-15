import styles from "./OfferCard.module.css"
import { Card, CardHeader, CardBody, CardFooter, Divider, Button, Link } from "@nextui-org/react"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faClock, faPlaneDeparture } from "@fortawesome/free-solid-svg-icons"

export function OfferCard({offer}){
    
    const months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

    const dateString = offer["departures"][0].split("T")[0]
    const dateTime = new Date(dateString)
    const day = dateTime.getUTCDate()
    const month = months[dateTime.getUTCMonth()]
    const year = dateTime.getUTCFullYear()

    const destination = offer["destination_city"]
    const originAirport = offer["origin"]
    const destinationAirport = offer["destination"]
    const departure = `${day} ${month} ${year}`
    const departureTime = offer["departures"][0].split("T")[1].replace(":00", "")
    const price = offer["price"]
    const seatAvailability = offer["availability"]
    const connections = offer["connections"]
    const duration = offer["duration"]
    const cabinClass = offer["cabin_class"]
    const url = `https://www.aerolineas.com.ar/flights-offers?adt=1&inf=0&chd=0&flexDates=false&cabinClass=Economy&flightType=ONE_WAY&leg=${originAirport}-${destinationAirport}-${dateString.split("-").join("")}`

    return(
        <>
            <Card className={styles.card}>
                <CardHeader className={styles.cardHeader}>
                    <h2 className="uppercase font-bold text-3xl text-indigo-300">{destination}</h2>
                </CardHeader>
                <Divider />
                <CardBody className={styles.cardBody}>
                    <span className="font-bold text-lg"><FontAwesomeIcon className="text-lg text-blue-500 mr-2" icon={faPlaneDeparture} />{departure}</span>
                    <span className="font-bold flex items-center text-lg"><FontAwesomeIcon className="text-lg text-blue-500 mr-2" icon={faClock} />{departureTime}</span>
                    <span className=" text-lg">{originAirport} - {destinationAirport}</span>
                    <span className="text-lg">{cabinClass}</span>
                    {seatAvailability == 1 ?
                    <span>{seatAvailability} asiento</span> :
                    <span>{seatAvailability} asientos</span>}
                    {connections < 1 && <span>0 escalas</span>}
                    {connections > 1 && <span>{connections} escalas</span>}
                    {connections == 1 && <span>{connections} escala</span>}
                </CardBody>
                <Divider />
                <CardFooter className={styles.cardFooter}>
                    <span className="font-bold text-2xl text-orange-300">$ {price}</span>
                    <Button className="text-md font-bold text-indigo-300" size="md" radius="full" variant="bordered" color="primary" href={url} as={Link} isExternal>Comprar</Button>
                </CardFooter>
            </Card>
        </>
    )
}