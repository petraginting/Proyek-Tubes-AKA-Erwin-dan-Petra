import time
import sys
from decimal import Decimal, ROUND_HALF_UP

def menghitung_iterative(distance_km, resource_type, level):
    resources = {
        'wood': [157000, 315000, 472000, 630000],
        'corn': [157000, 315000, 472000, 630000],
        'stone': [130000, 200000, 354000, 472000],
        'gold': [50000, 105000, 157000, 210000]
    }
    
    # waktu pengumpulan 3 jam * 60 menit * 60 detik
    collection_time = Decimal('10800')  
    travel_time_per_km = Decimal('12')
    
    travel_time = (Decimal(str(distance_km)) * travel_time_per_km * Decimal('2')).quantize(Decimal('0.01'))
    total_time = (collection_time + travel_time).quantize(Decimal('0.01'))
    
    resource_amount = Decimal(str(resources[resource_type][level - 1]))
    efficiency = (resource_amount / total_time).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    return {
        'total_time_seconds': float(total_time),
        'resource_amount': int(resource_amount),
        'efficiency': float(efficiency),
        'collection_time': float(collection_time),
        'travel_time': float(travel_time)
    }

def menghitung_recursive(distance_km, resource_type, level):
    resources = {
        'wood': [157000, 315000, 472000, 630000],
        'corn': [157000, 315000, 472000, 630000],
        'stone': [130000, 200000, 354000, 472000],
        'gold': [50000, 105000, 157000, 210000]
    }
    
    def calculate_travel_time(dist):
        if dist <= 0:
            return Decimal('0')
        return Decimal('12') + calculate_travel_time(dist - 1)
    
    collection_time = Decimal('10800')
    travel_time = calculate_travel_time(distance_km) * Decimal('2')
    total_time = (collection_time + travel_time).quantize(Decimal('0.01'))
    resource_amount = Decimal(str(resources[resource_type][level - 1]))
    efficiency = (resource_amount / total_time).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    return {
        'total_time_seconds': float(total_time),
        'resource_amount': int(resource_amount),
        'efficiency': float(efficiency),
        'collection_time': float(collection_time),
        'travel_time': float(travel_time)
    }

def format_time(seconds):
    seconds = Decimal(str(seconds))
    hours = int(seconds // Decimal('3600'))
    minutes = int((seconds % Decimal('3600')) // Decimal('60'))
    secs = int(seconds % Decimal('60'))
    return f"{hours}h {minutes}m {secs}s"

def main():
    sys.setrecursionlimit(20000)
    
    while True:
        print("\nRise of Kingdoms Resource Calculator")
        print("-----------------------------------")
        
        try:
            while True:
                try:
                    distance = int(input("Masukkan jarak (km): "))
                    if distance <= 0:
                        print("Error: Jarak harus lebih dari 0 km")
                    elif distance > 10000:
                        print("Error: Jarak maksimum adalah 10000 km")
                    else:
                        break
                except ValueError:
                    print("Error: Masukkan angka bulat untuk jarak")
                    
            print("\nPilih jenis sumber daya:")
            print("1. Wood (Kayu)")
            print("2. Corn (Jagung)")
            print("3. Stone (Batu)")
            print("4. Gold (Emas)")
            
            while True:
                try:
                    resource_choice = int(input("Masukkan pilihan (1-4): "))
                    if 1 <= resource_choice <= 4:
                        break
                    print("Error: Pilihan harus antara 1-4")
                except ValueError:
                    print("Error: Masukkan angka bulat untuk pilihan")
                
            resource_types = ['wood', 'corn', 'stone', 'gold']
            resource_type = resource_types[resource_choice - 1]
            
            while True:
                try:
                    level = int(input("Masukkan level sumber daya (1-4): "))
                    if 1 <= level <= 4:
                        break
                    print("Error: Level harus antara 1-4")
                except ValueError:
                    print("Error: Masukkan angka bulat untuk level")
            
            # Menghitung menggunakan algoritma iteratif dan rekursif
            start_time = time.perf_counter()
            iterative_result = menghitung_iterative(distance, resource_type, level)
            iterative_execution_time = time.perf_counter() - start_time
            
            start_time = time.perf_counter()
            recursive_result = menghitung_recursive(distance, resource_type, level) 
            recursive_execution_time = time.perf_counter() - start_time
            
            print("\nHasil Perhitungan:")
            print("-----------------")
            print("Metode Iteratif:")
            print(f"Waktu perjalanan: {format_time(iterative_result['travel_time'])}")
            print(f"Waktu pengumpulan: {format_time(iterative_result['collection_time'])}")
            print(f"Total waktu: {format_time(iterative_result['total_time_seconds'])}")
            print(f"Jumlah sumber daya: {iterative_result['resource_amount']:,}")
            print(f"Efisiensi: {iterative_result['efficiency']:.2f} resources/second")
            print(f"Waktu eksekusi: {iterative_execution_time:.6f} detik")
            
            print("\nMetode Rekursif:")
            print(f"Waktu perjalanan: {format_time(recursive_result['travel_time'])}")
            print(f"Waktu pengumpulan: {format_time(recursive_result['collection_time'])}")
            print(f"Total waktu: {format_time(recursive_result['total_time_seconds'])}")
            print(f"Jumlah sumber daya: {recursive_result['resource_amount']:,}")
            print(f"Efisiensi: {recursive_result['efficiency']:.2f} resources/second")
            print(f"Waktu eksekusi: {recursive_execution_time:.6f} detik")
            
            if iterative_execution_time > 0:
                print(f"\nMetode rekursif {(recursive_execution_time/iterative_execution_time):.2f}x lebih lambat")
            
        except Exception as e:
            print(f"Error: {str(e)}")
            
        choice = input("\nHitung lagi? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()