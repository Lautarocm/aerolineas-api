"use client"

import styles from "./Nav.module.css"
import { useState } from "react"
import { Navbar, NavbarMenu, NavbarMenuItem, NavbarContent, NavbarItem, NavbarMenuToggle, Link } from "@nextui-org/react"

export default function Nav(){

    const [isMenuOpen, setIsMenuOpen] = useState(false)

    const menuItems = [
        {
          href: "/",
          text: "Home"
        },
        {
          href: "/flights",
          text: "Vuelos"
        },
        {
          href: "/best-deals",
          text: "Más baratos"
        }
      ]

    return(

        <Navbar className={styles.navbar} onMenuOpenChange={setIsMenuOpen}>
            <NavbarContent>
                <NavbarMenuToggle
                aria-label={isMenuOpen ? "Close menu" : "Open menu"}
                className="sm:hidden" />
            </NavbarContent>
            <NavbarContent className="hidden sm:flex gap-4" justify="center">
                <NavbarItem>
                    <Link href="/" color="foreground">
                        Home
                    </Link>
                </NavbarItem>
                <NavbarItem>
                    <Link href="/flights" color="foreground">
                        Vuelos
                    </Link>
                </NavbarItem>
                <NavbarItem>
                    <Link href="/best-deals" color="foreground">
                        Más baratos
                    </Link>
                </NavbarItem>
            </NavbarContent>
            <NavbarMenu>
                {menuItems.map((item, index) => (
                    <NavbarMenuItem key={`${item}-${index}`}>
                        <Link
                        color="foreground"
                        className="w-full text-3xl mt-4"
                        href={item["href"]}
                        size="lg">
                            {item["text"]}
                        </Link>
                    </NavbarMenuItem>
                ))}
            </NavbarMenu>
        </Navbar>
    )
}