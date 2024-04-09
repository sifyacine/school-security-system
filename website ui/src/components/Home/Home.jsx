import React from 'react'
import HeroSection from './components/HeroSection'
import Advantages from './components/Advantages'
import { Box } from '@chakra-ui/react'

export default function Home() {
  return (
    <Box py={'5em'}>
    <HeroSection/>
    <Advantages/>
    </Box>
  )
}
