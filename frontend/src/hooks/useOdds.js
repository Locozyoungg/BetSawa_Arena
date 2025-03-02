// Custom hook for fetching live odds
import { useState, useEffect } from 'react';
import axios from 'axios';

export const useOdds = (sportType) => {
  const [odds, setOdds] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchOdds = async () => {
      try {
        const response = await axios.get(`/api/odds?type=${sportType}`);
        setOdds(response.data);
      } catch (error) {
        console.error('Error fetching odds:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchOdds();
  }, [sportType]);

  return { odds, loading };
};
