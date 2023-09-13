import { useState } from "react"

export function useSort() {

    const [sorted, setSorted] = useState(false)

    const handleSort = () => {
      setSorted((state) => {
        handleSort(!state)
        return !state
      })
    }

    const resetSort = () => {
      setSorted(false)
    }

  return {sorted, handleSort, resetSort}
}
