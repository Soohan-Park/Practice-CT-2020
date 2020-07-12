# Solved.

# 리스트 비어있는지 확인
isEmpty = lambda x : True if len(x) == 0 else False


def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = []  # 다리 위에서 트럭들이 다리를 건너는데 남은 시간
    onBridgeWeight = []  # 다리 위를 건너고 있는 트럭들의 무게 (순서 유지)

    while True:
        answer += 1
        if isEmpty(truck_weights) and isEmpty(onBridge) : break  # 건너고 있거나, 대기중인 차량이 없으면 BREAK

        # 대기중인 트럭이 있으면서, 다리 위 트럭들의 총 무게와 진입하려는 트럭의 무게가 총 무게를 넘지 않는다면 다리 진입
        if not isEmpty(truck_weights) and (truck_weights[0] + sum(onBridgeWeight)) <= weight:
            truckWeight = truck_weights.pop(0)
            onBridge.append(bridge_length)
            onBridgeWeight.append(truckWeight)

        # 다리 위 트럭들의 남은 시간 감소
        if not isEmpty(onBridge):
            onBridge = [ x - 1 for x in onBridge ]

        # 선두 트럭이 모두 건넜으면, 리스트들에서 제거
        if onBridge[0] == 0:
            onBridge.pop(0)
            onBridgeWeight.pop(0)

    return answer


if __name__ == '__main__':
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    print(solution(2, 10, [7, 4, 5, 6]))
