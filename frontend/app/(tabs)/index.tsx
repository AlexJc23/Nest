import { Image } from 'expo-image';
import { Platform, StyleSheet } from 'react-native';
import { useEffect, useState } from 'react';
import { HelloWave } from '@/components/hello-wave';
import ParallaxScrollView from '@/components/parallax-scroll-view';
import { Text } from 'react-native';
import { ThemedView } from '@/components/themed-view';

import { Link } from 'expo-router';
import { apiGet } from '@/src/api/client';


export default function HomeScreen() {
  const [status, setStatus] = useState<string | null>(null);

  useEffect(() => {
    async function loadStatus() {
      const data = await apiGet('/health');
      setStatus(data.status);
    }

    loadStatus();
  }, []);
  return (
    <Text style={{ fontSize: 20, fontWeight: 'bold', textAlign: 'center', marginTop: 100 }}>
      {status ? status : 'Loading...'}
    </Text>
  );
}

const styles = StyleSheet.create({
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
});
